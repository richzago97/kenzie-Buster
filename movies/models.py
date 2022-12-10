from django.db import models


class RatingChoice(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoice.choices,
        default=RatingChoice.G,
        null=True,
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    orders = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="ordened_movies",
    )

    def __str__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"

    def __repr__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"


class MovieOrder(models.Model):
    class Meta:
        verbose_name = "Movie Order"
        verbose_name_plural = "Movie Orders"

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_orders",
    )

    order = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_orders",
    )

    buyed_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"

    def __repr__(self) -> str:
        return f"<MovieOrder [{self.id}] - {self.price}>"
