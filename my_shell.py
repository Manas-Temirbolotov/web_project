m = Item(name="Pen", price="50")
m.save()
w = Item(name="Phone", price="100")
w.save()
u = Item(name="watch", price="300")
u.save()
o = Item(name="headphones", price="200")
o.save()
t = Item(name="hat", price="120")
t.save()

c = Purchase(item=m, name="Manas", age="38", date_purchase=timezone.now())
c.save()
c1 = Purchase(item=w, name="Almaz", age="18", date_purchase=timezone.now())
c1.save()
c2 = Purchase(item=u, name="Iskander", age="19", date_purchase=timezone.now())
c2.save()
c3 = Purchase(item=o, name="Belek", age="39", date_purchase=timezone.now())
c3.save()
c4 = Purchase(item=t, name="Aida", age="25", date_purchase=timezone.now())
c4.save()
c5 = Purchase.objects.create(item=m, name="Zulayka", age="22", date_purchase=timezone.now())
c6 = Purchase.objects.create(item=w, name="Sadyr", age="20", date_purchase=timezone.now())
c7 = u.purchase_set.create(name="Ruslan", age="30", date_purchase=timezone.now())
c8 = u.purchase_set.create(name="Kutman", age="40", date_purchase=timezone.now())
c8 = o.purchase_set.create(name="Roni", age="22", date_purchase=timezone.now())