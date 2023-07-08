from ..core.main import Step
from ..core.sdk import Models, ContinueSDK
from .main import UserInputStep
from ..recipes.CreatePipelineRecipe.main import CreatePipelineRecipe
from ..recipes.DDtoBQRecipe.main import DDtoBQRecipe
from ..recipes.DeployPipelineAirflowRecipe.main import DeployPipelineAirflowRecipe
from ..recipes.DDtoBQRecipe.main import DDtoBQRecipe
from ..recipes.AddTransformRecipe.main import AddTransformRecipe


class StepsOnStartupStep(Step):
    hide: bool = True

    async def describe(self, models: Models):
        return "Running steps on startup"

    async def run(self, sdk: ContinueSDK):
        steps_on_startup = sdk.config.steps_on_startup

        for step_type in steps_on_startup:
            step = step_type()
            await sdk.run_step(step)
