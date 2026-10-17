def calculate_average(values):
    if not values:
        raise ValueError("Lista ei saa olla tyhjä")

    return sum(values) / len(values)


def classify_score(score):
    if score < 0 or score > 100:
        raise ValueError("Pisteiden pitää olla välillä 0-100")

    if score < 50:
        return "hylätty"

    if score < 80:
        return "hyväksytty"

    return "erinomainen"


if __name__ == "__main__":
    print(classify_score(85))
