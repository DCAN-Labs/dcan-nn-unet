filelist = ls; 
files = split(filelist);
pat = "_0000.nii.gz";
for i = 1 : length(files)
    input_file = files(i);
    if endsWith(input_file, pat)
        newStr = extractBetween(input_file, '', pat);
        output_file = [char(newStr), '_0002'];
        monthsStr = char(extractBetween(newStr, '', 'mo'));
        voxelValue = 128;
        if strcmp(monthsStr, '00-02')
            voxelValue = int16(255 / 8);
        else 
            months = str2num(monthsStr);
            voxelValue = int16(months * 255 / 8);
        end

        make_blank_nifti(char(input_file), voxelValue, output_file)
    end
end
