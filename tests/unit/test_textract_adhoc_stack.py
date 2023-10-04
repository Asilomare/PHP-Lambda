import aws_cdk as core
import aws_cdk.assertions as assertions

from textract_adhoc.textract_adhoc_stack import TextractAdhocStack

# example tests. To run these tests, uncomment this file along with the example
# resource in textract_adhoc/textract_adhoc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TextractAdhocStack(app, "textract-adhoc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
