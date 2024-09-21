def kwargs_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

kwargs_info(name="ironman",power="fly \n")
kwargs_info(name="ironman\n")
kwargs_info(name="thor",power="hammer",enemy="loki")