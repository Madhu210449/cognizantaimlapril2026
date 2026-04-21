#create pipeline runner to display customer data from src.stores.customer_store_impl import CustomerStoreImpl

class PipelineRunner:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)
    def run(self,**kwargs):
        for stage in self.stages:
            data = stage(**kwargs)
        return data
        