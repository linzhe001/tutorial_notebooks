import open3d as o3d

def changing_file_type(input_path, output_path, num_points, view_or_not): #view or not: 1 to view, 0 to close
    mesh = o3d.io.read_triangle_mesh(input_path)
    pcd = mesh.sample_points_uniformly(number_of_points=num_points)
    o3d.io.write_point_cloud(output_path, pcd)
    if view_or_not:
        o3d.visualization.draw_geometries([pcd],
            window_name="Point Cloud Viewer",
            width=1024,
            height=768,
            left=50,
            top=50)

if __name__ == "__main__":
    input_path = r"C:\Users\asus\Downloads\full_model.obj"
    output_path = "./example.pcd"
    num_points = 10000
    changing_file_type(input_path,output_path,num_points,1)
    point_cloud = o3d.io.read_point_cloud(output_path)

        