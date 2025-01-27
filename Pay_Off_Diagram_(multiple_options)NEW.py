import streamlit as st
import opstrat as op

#st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Pay Off Diagram for Options",
    page_icon="💰",
    layout="wide",
)

# dashboard title
st.title(':rainbow[*_Pay Off Diagram for Options_*]😎')

spot_price = st.sidebar.number_input('**Spot Price**', value=100.00, step=0.5)

list_of_options = []

st.sidebar.write('**Options to plot**')
checks = st.sidebar.columns(4)
with checks[0]:
    option_no_1 = st.checkbox('1st', key="check_op_1", value=True)
    list_of_options.append(option_no_1)
with checks[1]:
    option_no_2 = st.checkbox('2nd', key="check_op_2")
    list_of_options.append(option_no_2)
with checks[2]:
    option_no_3 = st.checkbox('3rd', key="check_op_3")
    list_of_options.append(option_no_3)
with checks[3]:
    option_no_4 = st.checkbox('4th', key="check_op_4")
    list_of_options.append(option_no_4)

st.sidebar.divider()

zoom = st.sidebar.slider('**Zoom**', 0, 100, 90)

st.sidebar.divider()

# For Option 1
st.sidebar.subheader("For 1st Option")
option_type_1 = st.sidebar.radio(
    "**Option Type**",
    ["Call", "Put"],
    horizontal=True,
    key="op_type_1"
    )
if option_type_1=="Call":
    option_type_1="c"
elif option_type_1=="Put": 
    option_type_1="p"


position_1 = st.sidebar.radio(
    "**Position**",
    [":green[Long]", ":red[Short]"],
    horizontal=True,
    key="pos_1"
    )
if position_1==":green[Long]":
    position_1="b"
elif position_1==":red[Short]": 
    position_1="s"

strike_price_1 = st.sidebar.number_input('**Strike Price**', value=102.00, key="sp_1")

premium_1 = st.sidebar.number_input('**Premium**', value=1.00, key="prem_1")

st.sidebar.divider()

# For Option 2
st.sidebar.subheader("For 2nd Option")
option_type_2 = st.sidebar.radio(
    "**Option Type**",
    ["Call", "Put"],
    horizontal=True,
    index=None,
    key="op_type_2"
    )
if option_type_2=="Call":
    option_type_2="c"
elif option_type_2=="Put": 
    option_type_2="p"


position_2 = st.sidebar.radio(
    "**Position**",
    [":green[Long]", ":red[Short]"],
    horizontal=True,
    index=None,
    key="pos_2"
    )
if position_2==":green[Long]":
    position_2="b"
elif position_2==":red[Short]": 
    position_2="s"

strike_price_2 = st.sidebar.number_input('**Strike Price**', key="sp_2")

premium_2 = st.sidebar.number_input('**Premium**', key="prem_2")

st.sidebar.divider()

# For Option 3
st.sidebar.subheader("For 3rd Option")
option_type_3 = st.sidebar.radio(
    "**Option Type**",
    ["Call", "Put"],
    horizontal=True,
    index=None,
    key="op_type_3"
    )
if option_type_3=="Call":
    option_type_3="c"
elif option_type_3=="Put": 
    option_type_3="p"


position_3 = st.sidebar.radio(
    "**Position**",
    [":green[Long]", ":red[Short]"],
    horizontal=True,
    index=None,
    key="pos_3"
    )
if position_3==":green[Long]":
    position_3="b"
elif position_3==":red[Short]": 
    position_3="s"

strike_price_3 = st.sidebar.number_input('**Strike Price**', key="sp_3")

premium_3 = st.sidebar.number_input('**Premium**', key="prem_3")

st.sidebar.divider()

# For Option 4
st.sidebar.subheader("For 4th Option")
option_type_4 = st.sidebar.radio(
    "**Option Type**",
    ["Call", "Put"],
    horizontal=True,
    index=None,
    key="op_type_4"
    )
if option_type_4=="Call":
    option_type_4="c"
elif option_type_4=="Put": 
    option_type_4="p"


position_4 = st.sidebar.radio(
    "**Position**",
    [":green[Long]", ":red[Short]"],
    horizontal=True,
    index=None,
    key="pos_4"
    )
if position_4==":green[Long]":
    position_4="b"
elif position_4==":red[Short]": 
    position_4="s"

strike_price_4 = st.sidebar.number_input('**Strike Price**', key="sp_4")

premium_4 = st.sidebar.number_input('**Premium**', key="prem_4")

st.sidebar.divider()

if st.sidebar.button("Execute", type="primary"):
    st.snow()
    op_list = []
    if list_of_options[0] == True:
        op1={'op_type': option_type_1, 'strike': strike_price_1, 'tr_type': position_1, 'op_pr': premium_1}
        op_list.append(op1)
    if list_of_options[1] == True:
        op2={'op_type': option_type_2, 'strike': strike_price_2, 'tr_type': position_2, 'op_pr': premium_2}
        op_list.append(op2)
    if list_of_options[2] == True:
        op3={'op_type': option_type_3, 'strike': strike_price_3, 'tr_type': position_3, 'op_pr': premium_3}
        op_list.append(op3)
    if list_of_options[3] == True:
        op4={'op_type': option_type_4, 'strike': strike_price_4, 'tr_type': position_4, 'op_pr': premium_4}
        op_list.append(op4)
        
    # st.write(op_list)

    figure = op.multi_plotter(spot=spot_price, spot_range=100-int(zoom), op_list=op_list)
    st.pyplot(figure)

    st.toast('Diagram plotted!', icon='✅')


st.caption('**🟩 : Profit 🟥 : Loss**')
