-- Creates trigger that decreases quantity of item after adding new order
-- DROP TRIGGER IF EXISTS reduce quantity;
CREATE TRIGGER reduce_item AFTER INSERT ON orders FOR EACH ROW UPDATE items SET items.quantity = items.quantity - NEW.number WHERE items.name = NEW.item_name;
