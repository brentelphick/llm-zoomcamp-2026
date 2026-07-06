# Homework: 03 Orchestration

## Question 1: After trying the same prompt in ChatGPT vs Kestra AI Copilot, what is the primary reason AI Copilot generates better Kestra flows?

>    * AI Copilot uses a more powerful model
>    * AI Copilot has access to current Kestra plugin documentation
>    * AI Copilot uses more tokens
>    * AI Copilot has internet access

Answer: AI Copilot has access to current Kestra plugin documentation.


## Question 2: The non-RAG response about Kestra 1.1 features is best described as: (1 point)
>    * Accurate and specific, matching the actual release notes
>    * Vague, generic, or fabricated — the model guesses from training data
>    * Empty — the model refuses to answer without context
>    * Identical to the RAG version

Answer: Accurate and specific, matching the actual release notes


## Question 3. What is the approximate output token count for multilingual_agent when running with summary_length = short? (1 point)
>    * 5-15 tokens
>    * 60-100 tokens
>    * 200-400 tokens
>    * 500+ tokens

Answer: 123 so we say 60-100 is the closest.


## Question 4. With summary_length = long, roughly how many times more output tokens does multilingual_agent use compared to the short summary? (1 point)
>    * About the same (within 20%)
>    * 2-5x more
>    * 10-20x more
>    * 50x more

The short summary took 46 tokens. The long summary took 177 tokens, or about 3.8 times more than the short summary.

Answer: 2-5x more


## Question 5. After changing english_brevity to ask for 3 sentences instead of 1, how does the output token count compare to the original 1-sentence version? (1 point)
>    * About the same (within 20%)
>    * 2-4x more
>    * 5-10x more
>    * 10x+ more

With the 3-sentence summary and summary_length=long, the english_brevity task took 100 output tokens. With a 1-sentence summary the english_brevity task took 46 output tokens. This is approximately 2x.

Answer: 2-4x more


## Question 6. For production workflows requiring deterministic, repeatable results with strict compliance requirements, which approach is most appropriate? (1 point)
>    * Always use AI agents for maximum flexibility and adaptation
>    * Use traditional task-based workflows for predictability and auditability
>    * Use only RAG without agents for better performance
>    * Use web search tools exclusively to ensure current data

AI agents are not deterministic I don't think.

Answer: Use traditional task-based workflows for predictability and auditability
