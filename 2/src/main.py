from pyspark.sql.functions import col
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

spark = SparkSession.builder.getOrCreate()


def main():
    products_df = spark.createDataFrame(
        [
            (1, "Продукт A"),
            (2, "Продукт B"),
            (3, "Продукт C"),
            (4, "Продукт D"),
        ],
        schema=["product_id", "product_name"],
    )
    categories_df = spark.createDataFrame(
        [
            (1, "Категория 1"),
            (2, "Категория 2"),
            (3, "Категория 3"),
        ],
        schema=["category_id", "category_name"],
    )
    links_df = spark.createDataFrame(
        [
            (1, 1),
            (1, 2),
            (2, 1),
            (3, 2),
        ],
        schema=["product_id", "category_id"],
    )

    return products_df, categories_df, links_df


def get_products_with_categories(
    products_df: DataFrame,
    categories_df: DataFrame,
    links_df: DataFrame,
) -> DataFrame:
    """Возвращает Dataframe где есть все пары «Имя продукта – Имя категории» и
    имена всех продуктов, у которых нет категорий."""
    products_with_categories = (
        products_df.join(
            links_df,
            on="product_id",
            how="left",
        )
        .join(
            categories_df,
            on="category_id",
            how="left",
        )
        .select(
            col("product_name"),
            col("category_name"),
        )
    )

    return products_with_categories


if __name__ == "__main__":
    products_df, categories_df, links_df = main()
    result = get_products_with_categories(products_df, categories_df, links_df)
    result.show()
