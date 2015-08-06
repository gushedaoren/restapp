__author__ = 'oliver'
class ResponseTool:
    @staticmethod
    def getResultContent(statusCode,msg):
         content = {
                'status': statusCode,
                'msg': msg,
            }
         return content