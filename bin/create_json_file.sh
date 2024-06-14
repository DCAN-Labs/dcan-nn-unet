export nnUNet_raw_data_base="/scratch.global/hendr522-BIBSNet-T2only/"
export nnUNet_preprocessed="/scratch.global/hendr522-BIBSNet-T2only/nnUNet_preprocessed/"
export RESULTS_FOLDER="/home/feczk001/shared/data/nnUNet/nnUNet_raw_data_base/nnUNet_trained_models"

conda activate nnunet-env
cd /home/miran045/reine097/projects/abcd-nn-unet/dcan/dataset_conversion/
export PYTHONPATH="${PYTHONPATH}:."
python dcan.dataset_conversion.utils.generate_dataset_json(dataset.json, images_tr_dir: str, images_ts_dir: str, modalities: Tuple,
                          labels: dict, dataset_name: str, lcns: str = "hands off!", dataset_description: str = "",
                          dataset_reference="", dataset_release='0.0')
