from extract import extract_product,extract_users
from transform import transform_product,transform_users
from load import load_to_postgres


def run_pipeline():
    print("starting pipeline")

    product_df =extract_product()
    user_df =extract_users()

    print("starting transformation")

    product_df =transform_product(product_df)
    user_df = transform_users(user_df)

    print("loading to postgres......")

    load_to_postgres(product_df, "products")
    load_to_postgres(user_df, "users")

    print("ETL pipeline completed")

if __name__ == '__main__':
    run_pipeline()

