from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines
from .webservice_stage import WebServiceStage
class PipelineStack(core.Stack):
    def __init__(self, scope: core.Construct , id: str , **kwargs):
        super().__init__(scope,id,**kwargs)
        source_artifact=codepipeline.Artifact()
        cloud_assembly_artifact =codepipeline.Artifact()
        pipeline = pipelines.CdkPipeline(self,'Pipeline',

        cloud_assembly_artifact = cloud_assembly_artifact,
        pipeline_name='webinarPipeline',


        source_action=cpactions.GitHubSourceAction(
            action_name= 'Github',
            output=source_artifact,
            oauth_token=core.SecretValue.secrets_manager('github-token'),
            owner='akashdeepconnect',
            repo='cdkpipeline',
            trigger=cpactions.GitHubTrigger.POLL
            ),


        synth_action=pipelines.SimpleSynthAction(
            source_artifact=source_artifact,
            cloud_assembly_artifact=cloud_assembly_artifact,
            install_command='npm install -g aws-cdk && pip install -r requirements.txt',
            synth_command='cdk synth'
        )
        )

        pipeline.add_application_stage(WebServiceStage(self, 'l2', env={

            'account': '743708639786',
            'region': 'us-east-1'
        }))
