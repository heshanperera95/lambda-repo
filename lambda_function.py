import json

def lambda_handler(event, context):
    """
    Lambda function to process a JSON input and return a response.
    """
    try:
        # Extract fields from the input JSON
        name = event.get('name', 'Guest')
        age = event.get('age', None)
        interests = event.get('interests', [])
        
        # Create a response message
        if age:
            message = f"Hello, {name}! This is Version 3 You are {age} years old."
        else:
            message = f"Hello, {name}!"
        
        if interests:
            message += f" Your interests include: {', '.join(interests)}."
        
        # Return a response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": message,
                "input": event
            })
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e),
                "input": event
            })
        }
 