# Pointer Acceleration Configurator

This is a small web-based application built with [Streamlit](https://streamlit.io/) for configuring the `pointing_acceleration` module used in [zmk_pointing_acceleration](https://github.com/oleksandrmaslov/zmk-pointing-acceleration) ZMK based keyboards with trackpads. The app allows users to visually adjust acceleration parameters and generate a Device Tree Source (DTS) configuration for use in ZMK.

## Features

- **Interactive Sliders**: Adjust parameters such as `min-factor`, `max-factor`, `speed-threshold`, `speed-max`, and `acceleration-exponent` using an intuitive sidebar.
- **Real-Time Visualization**: View a dynamic graph of the acceleration factor as a function of speed.
- **DTS Configuration Generator**: Automatically generate a DTS snippet based on the selected parameters.
- **Copy-Friendly Output**: Easily copy the generated DTS configuration for use in your ZMK firmware or trackpad setup file.

## How to Run

#Click on this link: https://pointing.streamlit.app/
