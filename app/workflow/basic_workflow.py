from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)

class MyWorkflow(Workflow):
    @step
    async def my_step(self, ev: StartEvent) -> StopEvent:
        # do something here
        return StopEvent(result="Hello, world!")


w = MyWorkflow(timeout=10, verbose=False)
result = w.run()
print(result)