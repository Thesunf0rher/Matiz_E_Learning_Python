def build_profile(first, last, **kwargs):
    kwargs['first_name'] =  first
    kwargs['last_name'] =  last
    return kwargs

user_info = build_profile('Raim','kad',
                          age=19,
                          location='kz'
                          )

print(user_info)