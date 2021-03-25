from aws_cdk import core
from .akash_pipeline_stack import AkashPipelineStack
class WebServiceStage(core.Stage):
    def __init__(self, scope: core.Construct, id:str, **kwargs):
        super().__init__(scope,id,**kwargs)
        service=AkashPipelineStack(self,'')
        self.url_output =  service.url_output
