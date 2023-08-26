from llama import LLMEngine, Type, Context

class Test(Type):
    test_string: str = Context("just a test")

llm = LLMEngine(id="my_test")
#llm = LLMEngine(
#    id="my_test",
#    config={"production.key": "09631de17832509fdf5c0e3a690f273994b45f5f"}
#    )

test = Test(test_string="testing 123")
llm(test, output_type=Test)
