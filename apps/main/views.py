import requests
from bs4 import BeautifulSoup
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactSerializer, ReviewCreateSerializer


class GetPlayersRating(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        data = {}

        for count in range(1, 3):
            url = f"https://www.chess.com/ratings?page={count}"

            response = requests.get(url)

            soup = BeautifulSoup(response.content, "html.parser")

            players = soup.find_all("a", {"class": "master-players-rating-username"})
            ratings = soup.find_all(
                "div", {"class": "master-players-rating-player-rank master-players-rating-rank-active"}
            )

            for i in range(len(players)):
                full_name = players[i].text.replace("\n", "").strip()
                rating_score = ratings[i].text.replace("\n", "").strip()

                data[f"player_{(count-1)*50+i+1}"] = {
                    "order_number": (count - 1) * 50 + i + 1,
                    "full_name": full_name,
                    "rating_score": rating_score,
                }

        return Response({"data": data})


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer


class ReviewsCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
