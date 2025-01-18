import streamlit as st
import pandas as pd

def main():
    """
    Streamlit app to manage a list using st.dataframe.
    """

    st.title("List Manager with DataFrame")

    # Initialize list
    if "items" not in st.session_state:
        st.session_state.items = []

    # Add item
    new_item = st.text_input("Add item:")
    if st.button("Add"):
        st.session_state.items.append(new_item)
        st.experimental_rerun()

    # Display list in DataFrame
    df = pd.DataFrame(st.session_state.items, columns=["Items"])
    st.dataframe(df)

    # Select item (using index)
    if st.session_state.items:
        selected_index = st.number_input("Select item index to edit/delete (starting from 0):", 
                                         min_value=0, 
                                         max_value=len(st.session_state.items) - 1, 
                                         value=0, 
                                         step=1)

        # Edit item
        edited_item = st.text_input("Edit item:", value=st.session_state.items[selected_index])
        if st.button("Edit"):
            st.session_state.items[selected_index] = edited_item
            st.experimental_rerun()

        # Delete item
        if st.button("Delete"):
            del st.session_state.items[selected_index]
            st.experimental_rerun()

if __name__ == "__main__":
    main()