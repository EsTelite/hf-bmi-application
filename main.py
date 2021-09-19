import json

def lambda_handler(event, context):
    weight = event['queryStringParameters']['weight']
    height = event['queryStringParameters']['height']
    while True:
        try:
            weight = float(weight)
            height = float(height)
        except ValueError:
            return (return_builder_error("InappropriateValueError"))
        if weight < 0 or height < 0:
            return (return_builder_error("NegativeValueError"))
        elif weight == 0 or height == 0:
            return (return_builder_error("ZeroValueError"))
        else:
            bmi = bmi_calculate(weight, height)
            label = bmi_classifier(bmi)
            return (return_builder(bmi, label))

def bmi_classifier(bmi):
    if 18.5 <= bmi <= 24.9:
        return "healthy"
    elif bmi >= 25.0:
        return "overweight"
    elif bmi < 18.5:
        return "underweight"
    else:
        return "not classified"


def bmi_calculate(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 1)


def return_builder(bmi, label):
    data = {"bmi": bmi, "label": label}
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }


def return_builder_error(message):
    data = {"error": message}
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }