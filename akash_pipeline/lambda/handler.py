def handler(event,context):
    return{
        'body':'Hello from lambda!',
        'statusCode':'200'
    }

if __name__=='__main__':
    print(handler(event=None,context=None))