from mycroft import MycroftSkill, intent_file_handler


class SemanticKnowledge(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('knowledge.semantic.intent')
    def handle_knowledge_semantic(self, message):
        self.speak_dialog('knowledge.semantic')


def create_skill():
    return SemanticKnowledge()

