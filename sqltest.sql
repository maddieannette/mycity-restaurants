
select with_review.* 
from restaurants as with_review
join (
    select name,
    longitude,
    latitude,
    max(created_at) as last_poll
    from restaurants
    group by name, longitude, latitude
) as grouped_restaurants
    on with_review.name = grouped_restaurants.name
    and with_review.longitude = grouped_restaurants.longitude
    and with_review.latitude = grouped_restaurants.latitude
    and with_review.created_at = grouped_restaurants.last_poll
    where with_review.name = 'Marble Slab Creamery'