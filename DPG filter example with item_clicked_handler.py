import dearpygui.dearpygui as dpg

# dpg.get_platform() # --> Windows seems to be 0.

dpg.create_context()

def clicked_text():
    print("clicked me!")

def hover_call():
    print("hover")

with dpg.item_handler_registry(tag="click handler") as handler:
    dpg.add_item_clicked_handler(callback=clicked_text)

with dpg.item_handler_registry(tag="hover handler") as hover_handler:
    dpg.add_item_hover_handler(callback=hover_call)

def callback(sender, filter_string):
    dpg.set_value("filter_id", filter_string)

with dpg.window(label="about", width =500, height=300):
    dpg.add_input_text(label="Filter (inc, -exc)", callback=callback)
    with dpg.filter_set(id="filter_id"):
        dpg.add_text("aaa1.c", filter_key="aaa1.c", bullet=True)
        dpg.bind_item_handler_registry(dpg.last_item(),"click handler")
        dpg.bind_item_handler_registry(dpg.last_item(), "hover handler")

        dpg.add_text("bbb1.c", filter_key="bbb1.c", bullet=True)
        dpg.add_text("ccc1.c", filter_key="ccc1.c", bullet=True)
        dpg.add_text("aaa2.cpp", filter_key="aaa2.cpp", bullet=True)
        dpg.add_text("bbb2.cpp", filter_key="bbb2.cpp", bullet=True)
        dpg.add_text("ccc2.cpp", filter_key="ccc2.cpp", bullet=True)
        dpg.add_text("abc.h", filter_key="abc.h", bullet=True)
        dpg.add_text("hello, world", filter_key="hello, world", bullet=True)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()