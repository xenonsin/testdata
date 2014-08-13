import model
import datetime


def initialize():

    # Adding Restaurant

    res = model.Restaurant(name='Ten Ren');
    res.put();
    
    # Adding Menus

    din = model.Menu(restaurant = res, name = 'Dinner Menu')
    din.put();
    lun = model.Menu(restaurant = res, name = 'Lunch Menu')
    lun.put()

    # Adding Categories

    app = model.Category(name = 'Appetizers')
    app.menus.append(lun.key())
    app.put()

    sb = model.Category(name = 'Small Bites')
    sb.menus.append(din.key())
    sb.put()

    lb = model.Category(name = 'Large Bites')
    lb.menus.append(din.key())
    lb.put()

    # Addding Dishes

    eggRoll = model.Dish(name = 'Egg Roll')
    eggRoll.categories.append(app.key())
    eggRoll.categories.append(sb.key())
    eggRoll.restaurant = res
    eggRoll.put()

    chickenWings = model.Dish(name = 'Chicken Wings')
    chickenWings.categories.append(app.key())
    chickenWings.categories.append(lb.key())
    chickenWings.restaurant = res
    chickenWings.put()