from discount.models import Card
import csv


def update_profiles(file):
    card_set = Card.objects.all()
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                card_number = row[0]
                card_name = row[1]
                card_rating = row[2]
                for card in card_set:
                    if card.card_number == int(card_number):
                        card.rating += 1
                        card.save()

