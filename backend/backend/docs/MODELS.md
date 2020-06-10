Model Architecture planing 

Membership 
    -slug 
    -type (free, po,enterprise)
    -price 
    -strip_plan id

Usermembership
    -user (foreign key to default user)
    -strip customer id
    -membership type  (foreign key to default membership)

Subscription
    -user membership
    -strip subscription id  (foreign key to default usermembership)
    -active

Course
    -slug
    -title
    -desc
    -allowed memberships (fk memberships)

Lesson
    -slug
    -title
    -desc
    -Course (fk Course)
    -position
    -video
    -thumbnail

