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
        )
        
        api = apigw.LambdaRestApi(self, 'phpApi',
            handler=function
        )
        plan = api.add_usage_plan("UsagePlan")
        
        key = api.add_api_key("ApiKey",
            value="hjovtrvbkhljn345678inuf43txchexjn"
        )
        
        plan.add_api_key(key)
        
        # x-api-key: hjovtrvbkhljn345678inuf43txchexjn
        
        php_endpoint = api.root.add_resource("php")
        php_endpoint.add_method("GET", 
            api_key_required=True,
            request_parameters={
              'method.request.header.x-api-key': True,
            },
        )
        
        
        plan.add_api_stage(
            stage=api.deployment_stage
        )