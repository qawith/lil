init python:
    from pythonpackages.inventorysystem.inventory import InventoryItem
    from pythonpackages.inventorysystem.inventory import Inventory

### The format is name, description, icon image (if applicable), value (if applicable, selling/buying value), action (screen language action to be performed when icon is clicked on inventory screen), and recipe (if craftable).

### Items without icons are created like this:      
#$ quarter = InventoryItem("Quarter", "A new quarter)

define inventory_items = {
    ### Items with icons are created like this:
    "eye"       :   InventoryItem(name=__("Eyeball"), description=__("A human eyeball, how creepy!"), icon="images/eye.webp", value=250),
    # Items that can be used in crafting
    "but"       :   InventoryItem(__("Button"), __("A shiny button"), "images/button.webp", 100),
    "yarn"      :   InventoryItem(__("Yarn"), __("Yarny yarny yarn."), "images/yarn.webp", 30),
    "fabric"    :   InventoryItem(__("Fabric"), __("You know, cloth."), "images/fabric.webp", 100),
    "coin"      :   InventoryItem(__("Coin"), __("An old coin"), "images/coin.webp", 1),
    # An item with a unique action (shows screen with custom message)
    "sword"     :   InventoryItem(__("Awesome Sword"), __("An awesome sword."), "images/sword.webp", 500, Show("popup", message = __("You wave the sword around wildly but nothing happens."))),
    # An item that can be crafted has a recipe, which is a nested list of [ingredient, quantity]
    "necklace"  :   InventoryItem(__("Penny Necklace"), __("Super magic."), "images/necklace.webp", 50), #, recipe = [[coin,6],[yarn,1]]),
    "doll"      :   InventoryItem(__("Handmade Doll"), __("Guaranteed to bring luck. (Or not?) Very huggable, mind the needle."), "images/doll.webp", 100000), #, recipe = [[but,2],[fabric,3],[yarn,1]]),
}

######### DEFINE INVENTORIES ##########    
define mc_inventory_name = __("")
default mc_inventory = Inventory(name="[mc_inventory_name]", money=100, interest_percentage=0/100,
    inventoryItems = {
        "coin":     4,

    }
)

define shop_inventory_name = __("")
default shop_inv = Inventory(name="[shop_inventory_name]", money=500, interest_percentage=20/100,
    inventoryItems = {
    }
)
    
