my_set = []

def create_bucket(name: str, count: int) -> dict:
    bucket = {
        "bucket_name": name,
        "file_count": count
    }
    return bucket



if __name__ == "__main__":
    m = int(input())
    a = set(map(int, (input().split())))
    n = int(input())
    b = set(map(int, (input().split())))

    sorted_list = sorted(list(a.difference(b).union(b.difference(a))))
    for _ in sorted_list:
        print(_)

    bucketA = create_bucket("bucketA", 2)
    bucketB = create_bucket("bucketB", 1)
    bucketC = create_bucket("bucketC", 4)
    bucketD = create_bucket("bucketA", 5)
    my_set.append(bucketA)
    my_set.append(bucketB)
    my_set.append(bucketC)
    print(next((i for i in my_set if i.get("bucket_name") == "bucketA"), "None"))

    print(list(filter(lambda bucket: bucket["bucket_name"] == "bucketA", my_set))[0])