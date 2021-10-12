#!/usr/bin/env python3
from aws_cdk import core
from stacks import TemplateStack


app = core.App()
environment = app.node.try_get_context("environment")
TemplateStack(app, f"CDKTemplate{environment}")
app.synth()
