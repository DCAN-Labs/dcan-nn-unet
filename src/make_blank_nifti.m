function [] = make_blank_nifti(input_file, voxel_value, output_file)
%MAKE_BLANK_NIFTI Creates a 'blank' NIFTI file.
%   Creates a 'blank' NIFTI file the same size as the input file, with a
%   constant gray value throughout.
V = niftiread(input_file);
s = size(V);
for i = 1 : s(1)
    for j = 1 : s(2)
        for k = 1 : s(3)
            if V(i, j, k) ~= 0
                V(i, j, k) = voxel_value;
            end
        end
    end
end
info = niftiinfo(input_file);
niftiwrite(V, output_file, info)
output_file_with_extension = [output_file, '.nii'];
gzip(output_file_with_extension)
delete(output_file_with_extension)
end
