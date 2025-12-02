import streamlit as st
import time
import random

st.set_page_config(page_title="Procrastination Timer", page_icon="⏱️")

st.title("⏱️ Procrastination Timer")
st.write("A timer that fully supports your commitment to *not* getting things done.")

messages = [
    "You've worked hard enough. Take a break 😌",
    "Focus? Overrated. Rest your eyes.",
    "2 minutes of effort = lifetime achievement unlocked.",
    "You deserve a snack break. Maybe two.",
    "Hard work is important, but so is doing absolutely nothing.",
    "Don't rush. Procrastination is an art."
]

st.header("🎮 Start Timer")

minutes = st.slider("How long do you *pretend* to work?", 1, 60, 5)

if st.button("Start Procrastination Session"):
    with st.spinner("Pretending to be productive..."):
        for remaining in range(minutes * 60, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer_text = f"{mins:02d}:{secs:02d}"
            st.metric("Time remaining", timer_text)
            time.sleep(1)

    st.success("Time's up! Great job doing almost nothing! 🎉")
    st.write(random.choice(messages))

st.divider()
st.caption("Made with ❤️ and zero productivity in mind.")
