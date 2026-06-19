INSTRUCTIONS = '''
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
'''

PROMPT_TEMPLATE = '''
QUESTION: {question}

CONTEXT:
{context}
'''.strip()


class RAGABase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        model='gpt-5.4-mini',
        usage=None
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.prompt_template = prompt_template
        self.model = model
        self.usage = None

    def search(self, query, num_results=5):

        return self.index.search(
            query,
            num_results=num_results,
        )

    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append(doc['filename'] + ": " + doc['content'].replace('\n', ' '))
            lines.append('')

        return '\n'.join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, prompt):
        input_messages = [
            {'role': 'developer', 'content': self.instructions},
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )
        self.usage = response.usage
        return response

    def rag(self, query):
        print("Running RAG for query: {}".format(query))
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        response = self.llm(prompt)
        return response.output_text

    def wtf(self):
        print("Index: {}".format(self.index))
        print("LLM Client: {}".format(self.llm_client))
        print("Instructions: {}".format(self.instructions))
        print("Prompt Template: {}".format(self.prompt_template))
        print("Model: {}".format(self.model))

    def getUsage(self):
        return self.usage