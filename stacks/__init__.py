from aws_cdk import core
from aws_cdk import aws_lambda
from aws_cdk.aws_lambda_python import PythonFunction


class TemplateStack(core.Stack):
    def __init__(self, scope: core.Construct, _id: str, **kwargs) -> None:
        super().__init__(scope, _id, **kwargs)
        self._create_lambda()

    def _create_lambda(self):
        PythonFunction(
            self,
            "CDKTemplateFunction",
            entry="src",
            index="handler.py",
            handler="handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
        )
