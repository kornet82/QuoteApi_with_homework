from api import Resource, reqparse, db, auth
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from api.schemas.quote import quote_schema, quotes_schema


class QuoteResource(Resource):
    def get(self, author_id=None, quote_id=None):
        """
        Обрабатываем GET запросы
        :param author_id: id автора
        :param quote_id: id цитаты
        :return: http-response(json, статус)
        """
        if author_id is None and quote_id is None:  # Если запрос приходит по url: /quotes
            quotes = QuoteModel.query.all()
            # return [quote.to_dict() for quote in quotes]  # Возвращаем ВСЕ цитаты
            return quotes_schema.dump(quotes)  # Возвращаем ВСЕ цитаты

        author = AuthorModel.query.get(author_id)
        if quote_id is None:  # Если запрос приходит по url: /authors/<int:author_id>/quotes
            quotes = author.quotes.all()
            # return [quote.to_dict() for quote in quotes], 200  # Возвращаем все цитаты автора
            return quotes_schema.dump(quotes), 200  # Возвращаем все цитаты автора

        quote = QuoteModel.query.get(quote_id)
        if quote is not None:
            # return quote.to_dict(), 200
            return quote_schema.dump(quote), 200
        return {"Error": "Quote not found"}, 404

    @auth.login_required
    def post(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("text", required=True)
        quote_data = parser.parse_args()
        # TODO: раскомментируйте строку ниже, чтобы посмотреть quote_data
        #   print(f"{quote_data=}")
        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404

        quote = QuoteModel(author, quote_data["text"])
        db.session.add(quote)
        db.session.commit()
        return quote_schema.dump(quote), 201

    def put(self, author_id, quote_id):
        parser = reqparse.RequestParser()
        parser.add_argument("author_id")
        parser.add_argument("text")
        new_data = parser.parse_args()
        print (new_data)
        quote = QuoteModel.query.get(quote_id)
        quote.author = new_data["author_id"]
        quote.text = new_data["text"]
        db.session.commit()
        return quote_schema.dump(quote), 200

    def delete(self, quote_id):
        raise NotImplemented("Метод не реализован")
