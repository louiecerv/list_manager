import streamlit as st
from  listutils import add_item, edit_item, delete_item

# Initialize session state to store the list of items and new item
if 'item_list' not in st.session_state:
    st.session_state.item_list = []
if 'new_item' not in st.session_state:
    st.session_state.new_item = ''

def main():
    # Streamlit app
    st.title('Streamlit List App')

    # Create a tab for each action
    tab_add, tab_list, tab_edit = st.tabs(['Add Item', 'List of Items', 'Edit/Delete Item'])

    # Add new item tab
    with tab_add:
        st.header('Add New Item')
        st.session_state.new_item = st.text_input('Enter new item')
        st.button('Add', on_click=add_item)

    # List of items tab
    with tab_list:
        st.header('List of Items')
        for i, item in enumerate(st.session_state.item_list):
            st.write(f'{i+1}. {item}')

    # Edit or delete item tab
    with tab_edit:
        st.header('Edit or Delete Item')
        selected_item = st.selectbox('Select Item', st.session_state.item_list)
        if selected_item:
            index = st.session_state.item_list.index(selected_item)
            edit_value = st.text_input('Edit Item', value=selected_item)
            if st.button('Save Edit'):
                edit_item(index, edit_value)
            if st.button('Delete'):
                delete_item(index)

    if st.button("Show Items"):

        for item in st.session_state.item_list:
            st.write(f"Item: {item}")

if __name__ == '__main__':
    main()      