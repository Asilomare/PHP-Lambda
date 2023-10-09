#!/usr/bin/env python3
import os

import aws_cdk as cdk

from phpLambdaStack.phpLambdaStack import phpLambdaStack


app = cdk.App()
phpLambdaStack(app, "phpLambdaStack")

app.synth()
