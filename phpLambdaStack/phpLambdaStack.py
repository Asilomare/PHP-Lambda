from aws_cdk import (
    Duration,
    Stack,
   aws_lambda as _lambda,
   aws_s3 as s3,
   aws_iam as iam,
   aws_apigateway as apigw,
)
from constructs import Construct

class phpLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        function = _lambda.DockerImageFunction(self, 'phpLambda',
            code=_lambda.DockerImageCode.from_image_asset('lambda'),
            
            # More options
            # timeout=Duration.seconds(300),
            # memory_size=512,
        )
        
        api = apigw.LambdaRestApi(self, 'phpApi',
            handler=function
        )