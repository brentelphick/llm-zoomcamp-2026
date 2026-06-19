
class ZoomCampRAG:
    """ A class to help implement Retrieval Augmented Generation (RAG)
        for the ZoomCamp course.

        This class is modified from the RAGBase class in rag_helper.py
        to work with the specific structure of the augmented data index
        used in this course.

        Attributes:
            augmented_data_index: The full name of the employee.
            llm_client: An object that can call an LLM for the answer to
                life, the universe, and everything.
            instructions: System instructions for the LLM.
            prompt_template: Template for building the prompt.
            model: The LLM model to use. Default is 'gpt-5.4-mini' (which
                requires llm_client to be for OpenAI's API).
        """
    
    def __init__(
        self,
        augmented_data_index,
        llm_client,
        instructions,
        prompt_template,
        model='gpt-5.4-mini'
    ):
        self.augmented_data_index = augmented_data_index
        self.llm_client = llm_client
        self.instructions = instructions
        self.prompt_template = prompt_template
        self.model = model


    def query(self, question, num_results=5):

        # Search our augmented data index for relevant context
        search_results = self.__search(question, num_results)

        # Build the prompt to pass to the LLM. This includes the
        # overall system instruction, the user query and the
        # context data retrieved from our augmented data index.
        prompt = self.__build_prompt(question, search_results)

        # Ask the LLM to answer the question based on the retrieved
        # context
        response = self.__llm(prompt)

        return response.output_text, response.usage

    def __search(self, question, num_results):
        #boost_dict = {'content': 2.0, 'filename': 0.5}
        #filter_dict = {'filename': self.course}

        return self.augmented_data_index.search(
            question,
            num_results=num_results,
            #boost_dict=boost_dict,
            #filter_dict=filter_dict
        )

    def __build_prompt(self, question, search_results):
        context = self.__build_context(search_results)
        return self.prompt_template.format(
            question=question, context=context
        )

    def __build_context(self, search_results):
        lines = []

        # My pre-AI brain doesn't really understand why we need to format
        # the context data this way. I would have thought that a
        # 'machine-readable' format would be better, but apparently not.
        
        for doc in search_results:
            # We probably don't need to remove newlines, but if we did
            # want to filter by filename this might be more useful.
            
            # Having to do this within this class ties us too much to the
            # specific structure of the augmented data.
            lines.append(doc['filename'] + ": " + doc['content'].replace('\n', ' '))
            lines.append('')

        return '\n'.join(lines).strip()


    def __llm(self, prompt):
        input_messages = [
            {'role': 'developer', 'content': self.instructions},
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )
        return response

