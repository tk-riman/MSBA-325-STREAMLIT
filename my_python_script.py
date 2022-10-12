#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import plotly as pt
import plotly.express as px
import streamlit as st


# In[31]:


height_v_country = pd.read_csv("Height of Male and Female by Country 2022.csv")
tipping_dataset = pd.read_csv("tips.csv")
global_plastic_prod = pd.read_csv("global-plastics-production.csv")


# In[32]:


fig_1 = px.box(height_v_country, x="Male Height in Cm", title="Male Height in Cm")


# In[34]:


fig_2 = px.violin(height_v_country, y="Female Height in Cm", title="Female Height in Cm")


# In[36]:


fig_3 = px.histogram(height_v_country, x="Country Name", y="Male Height in Cm", title="Average Height Vs. Country")


# In[38]:


fig_4 = px.scatter(tipping_dataset, x="total_bill", y="tip", color="sex", size="size", title="Tip V. Total Bill")


# In[40]:


fig_5 = px.line(global_plastic_prod, x="Year", y="Global plastics production (million tonnes)", title="Global Plastic Generation V. Years")


# In[42]:


interactive_plot_1 = st.container()
interactive_plot_2 = st.container()
interactive_plot_3 = st.container()
interactive_plot_4 = st.container()
interactive_plot_5 = st.container()


# In[46]:


with interactive_plot_1:
    st.header("HavE you ever wondered whether your height is average or not?")
    st.text("Check this out, Let's start with the boys!")
    st.plotly_chart(fig_1, use_container_width=True)


# In[47]:


with interactive_plot_2:
    st.title("Now, let's check it for the girls!")
    st.plotly_chart(fig_2, use_container_width=True)


# In[67]:


with interactive_plot_3:
    st.title("Maybe a histogram can change our perspective")
    st.header("Don't be startled, this is the avergae of total heights per country!")
    st.plotly_chart(fig_3, use_container_width=True)
    st.dataframe(height_v_country)


# In[68]:


with interactive_plot_5:
    st.header("Is the plastic Waste Generation Increasing Throughout the Years?")
    st.text("it seems so, here we see that with the passage of time, more tonnes of plastic waste is generated")
    st.plotly_chart(fig_5, use_container_width=True)
    st.text("Click the Donate Button and Help Combat Plastic Waste")
    result = st.button("Donate Button")
    st.write(result)
    if result:
        st.write("https://crisisrelief.un.org/donate")
    


# In[65]:


with interactive_plot_4:
    st.header("Do tables with higher bills also tip higher?xd")
    option = st.multiselect('Select at least one account please', tipping_dataset['select_gender'].drop_duplicates())
    st.write('Your gender selected is:', option)
#option_2 = st.sidebar.multiselect('Now, select at least one bank', df['BANCO'].drop_duplicates())
#st.write('Your bank selected is:', option_2)  
    tipping_dataset = tipping_dataset[tipping_dataset['select_gender'].isin(option)]
    #df = df[df['BANCO'].isin(option_2)]
    fig_4 = px.scatter(tipping_dataset, x="total_bill", y="tip", color="sex", size="size", title="Tip V. Total Bill")
    st.plotly_chart(fig_4, use_container_width=True)
    yes_tip = st.checkbox("Yes!")
    no_tip = st.checkbox("No")
    if yes_tip:
        st.write("Great, as everyone should!")
    if no_tip:
        st.write("That's a shame, try it next time, and see the relieve in their eyes")

