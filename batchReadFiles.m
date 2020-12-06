path = [uigetdir(), '/'];
% path = input('????:', s);
file = dir(fullfile(path,'*.txt'));
fileNames = {file.name}';

lengthNames = size(fileNames, 1);

for k = 1:lengthNames
    kThFile = strcat(path, fileNames{k, 1});
    eval(['dt',strrep(fileNames{k, 1}, '.txt', ''),'=','load(kThFile)']);
end