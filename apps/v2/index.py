import demjson
import json

# str = """
# {
# id: 225,
# is_in_serving: true,
# description: "有菜有肉，营养均衡",
# title: "简餐",
# link: "eleme://restaurants?filter_key=%7B%22activity_types%22%3A%5B3%5D%2C%22category_schema%22%3A%7B%22category_name%22%3A%22%5Cu7b80%5Cu9910%22%2C%22complex_category_ids%22%3A%5B209%2C212%2C215%2C265%5D%2C%22is_show_all_category%22%3Atrue%7D%2C%22restaurant_category_id%22%3A%7B%22id%22%3A207%2C%22name%22%3A%22%5Cu5feb%5Cu9910%5Cu4fbf%5Cu5f53%22%2C%22sub_categories%22%3A%5B%5D%2C%22image_url%22%3A%22%22%7D%2C%22activities%22%3A%5B%7B%22id%22%3A3%2C%22name%22%3A%22%5Cu4e0b%5Cu5355%5Cu7acb%5Cu51cf%22%2C%22icon_name%22%3A%22%5Cu51cf%22%2C%22icon_color%22%3A%22f07373%22%2C%22is_need_filling%22%3A1%2C%22is_multi_choice%22%3A0%2C%22filter_value%22%3A3%2C%22filter_key%22%3A%22activity_types%22%7D%5D%7D&target_name=%E7%AE%80%E9%A4%90&animation_type=1&is_need_mark=0&banner_type=",
# image_url: "/d/38/7bddb07503aea4b711236348e2632jpeg.jpeg",
# icon_url: "",
# title_color: ""
# }
# """
#
# # print(demjson.decode(str))
# print(json.dumps(demjson.decode(str)))

if __name__ == '__main__':
    with open("./data.js","r",encoding="utf8") as f:
        for i in demjson.decode(f.read()):
            print(json.dumps(i))
