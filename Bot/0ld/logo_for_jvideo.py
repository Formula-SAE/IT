import vtk

# Define parameters
num_layers = 80  # Number of layers
layer_spacing = 0.03  # Spacing between layers
starting_color = (0.3, 0.81, 0.3)  # Starting color (green)
top_color = (1, 1, 1)  # Top layer color (white)

# Create a renderer and render window
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("3D Text Effect")
render_window.AddRenderer(renderer)


# Create a render window interactor
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Create a text source for the first part of the text
text_source_first = vtk.vtkVectorText()
text_first = "  Ap  \nCo"
text_source_first.SetText(text_first.upper())

# Create a text mapper for the first part
text_mapper_first = vtk.vtkPolyDataMapper()
text_mapper_first.SetInputConnection(text_source_first.GetOutputPort())

# Create a text source for the second part of the text
text_source_ex = vtk.vtkVectorText()
text_source_ex.SetText("ex".upper())

# Create a text mapper for the second part
text_mapper_second_ex = vtk.vtkPolyDataMapper()
text_mapper_second_ex.SetInputConnection(text_source_ex.GetOutputPort())

# Create a text source for the "R"
text_source_r = vtk.vtkVectorText()
text_r = "R"
text_source_r.SetText(text_r.upper())

# Create a text mapper for the "R"
text_mapper_r = vtk.vtkPolyDataMapper()
text_mapper_r.SetInputConnection(text_source_r.GetOutputPort())

# Create a text source for the second part of the text
text_source_second = vtk.vtkVectorText()
text_second = "\nse"
text_source_second.SetText(text_second.upper())

# Create a text mapper for the second part
text_mapper_second = vtk.vtkPolyDataMapper()
text_mapper_second.SetInputConnection(text_source_second.GetOutputPort())



# Create text actors for multiple layers with gradient color for the first part
for i in range(num_layers):
    if i == 0:
        layer_color = top_color
    else:
        # Calculate color for the current layer (darker tone of green)
        layer_color = tuple(starting_color[j] * ((i + 1) / num_layers) for j in range(3))

    # Create text actor for the first part
    text_actor_first = vtk.vtkActor()
    text_actor_first.SetMapper(text_mapper_first)
    text_actor_first.GetProperty().SetColor(layer_color)  # Set color for the layer
    text_actor_first.SetPosition(i * 0.009, 0, -(i * layer_spacing))  # Adjust position along z-axis
    renderer.AddActor(text_actor_first)


# Calculate the starting position for the second part of the text
start_position_second = len(text_first) / 2.98

# Create text actors for multiple layers with gradient color for the second part
for i in range(num_layers):
    if i == 0:
        layer_color = top_color
    else:
        # Calculate color for the current layer (darker tone of green)
        layer_color = tuple(starting_color[j] * ((i + 1) / num_layers) for j in range(3))

    # Create text actor for the second part
    text_actor_second_ex = vtk.vtkActor()
    text_actor_second_ex.SetMapper(text_mapper_second_ex)
    text_actor_second_ex.GetProperty().SetColor(layer_color)  # Set color for the layer
    text_actor_second_ex.SetPosition(start_position_second - i * 0.009, 0, -(i * layer_spacing))  # Adjust position along z-axis
    renderer.AddActor(text_actor_second_ex)


# Calculate the starting position for the "R"
start_position_r = len(text_first) / 3.7

# Create text actors for multiple layers with gradient color for the "R"
for i in range(num_layers):
    if i == 0:
        layer_color = top_color
    else:
        # Calculate color for the current layer (darker tone of green)
        layer_color = tuple(starting_color[j] * ((i + 1) / num_layers) for j in range(3))

    # Create text actor for the "R"
    text_actor_r = vtk.vtkActor()
    text_actor_r.SetMapper(text_mapper_r)
    text_actor_r.GetProperty().SetColor(layer_color)  # Set color for the layer
    text_actor_r.SetPosition(start_position_r, - start_position_r / 1.76, -(i * layer_spacing))  # Adjust position along z-axis
    renderer.AddActor(text_actor_r)

# Calculate the starting position for the second part of the text
start_position_second = len(text_first) / 2.47

# Create text actors for multiple layers with gradient color for the second part
for i in range(num_layers):
    if i == 0:
        layer_color = top_color
    else:
        # Calculate color for the current layer (darker tone of green)
        layer_color = tuple(starting_color[j] * ((i + 1) / num_layers) for j in range(3))

    # Create text actor for the second part
    text_actor_second = vtk.vtkActor()
    text_actor_second.SetMapper(text_mapper_second)
    text_actor_second.GetProperty().SetColor(layer_color)  # Set color for the layer
    text_actor_second.SetPosition(start_position_second - i * 0.009, 0, -(i * layer_spacing))  # Adjust position along z-axis
    renderer.AddActor(text_actor_second)




# Set background color to black
renderer.SetBackground(0, 0, 0)




# Enable depth testing
renderer.GetActiveCamera().SetPosition(-4, -12, 8)
renderer.GetActiveCamera().SetFocalPoint(2, 0, -1)
renderer.GetActiveCamera().SetViewUp(0, 1, 0.5)
renderer.GetActiveCamera().Azimuth(30)
renderer.GetActiveCamera().Elevation(30)
renderer.GetActiveCamera().Dolly(1.5)
renderer.ResetCamera()
renderer.ResetCameraClippingRange()

# Enable depth testing
renderer.UseDepthPeelingOn()
renderer.SetMaximumNumberOfPeels(100)
renderer.SetOcclusionRatio(0.1)

# Define mouse click event handler
def mouse_click_callback(obj, event):
    camera = renderer.GetActiveCamera()
    print("Updated Camera Position:", camera.GetPosition())
    print("Updated Camera Focal Point:", camera.GetFocalPoint())
    print("Updated Camera View Up:", camera.GetViewUp())

# Bind the mouse click event
render_window_interactor.AddObserver("LeftButtonPressEvent", mouse_click_callback)

# Start the interactor
render_window.Render()
render_window_interactor.Start()
