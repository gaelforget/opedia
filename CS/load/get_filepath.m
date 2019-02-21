function [rep nrt filepath] = get_filepath(iteration)
    repDataPath = 'H:/Dropbox (MIT)/Apps/opediaVault/observation/remote/satellite/alt/rep/rep_alt_';
    nrtDataPath = 'H:/Dropbox (MIT)/Apps/opediaVault/observation/remote/satellite/alt/nrt/nrt_alt_';
    repDataPath=strcat(repDataPath, sprintf('%7.7d',iteration),'.nc');   
    nrtDataPath=strcat(nrtDataPath, sprintf('%7.7d',iteration),'.nc');

    rep = file_exists(repDataPath);
    nrt = file_exists(nrtDataPath);
    
    filepath = repDataPath;             % first assumes that the reprocessed file exist
    if rep == false                     % if reprocessed file didn't exist, look for nrt file
        filepath = nrtDataPath; 
        assert(exist(filepath,'file') == 2, 'NetCDF file not found.' );
    else
        nrt = false;
    end    
    
  
end


