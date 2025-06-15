"""Local utilities for notebooks"""
from pathlib import Path
from enum import StrEnum
import unittest
import numpy as np
import pandas as pd


class Stage(StrEnum):
		"""Stage of the treatment

		Attributes:
			BEFORE: Before surgery
			DURING: During the surgery
			AFTER: After the surgery
		"""
		BEFORE = "BEFORE"
		DURING = "DURING"
		AFTER = "AFTER"


class Dataset:
	"""AA or AVM patients' dataset

	Attributes:
		path (pathlib.Path): Path object to traverse the dataset directory
		data (dict[str, dict[[utils.Stage, pd.DataFrame]]): Patients' code
			mapped to blood-flow data and indexed by the treatment `Stage` 
	"""
	def __init__(self, path: str):
		"""Load clinical data from a dataset directory

		Args:
			path: Path to the dataset directory
		"""
		self.path = Path(path)
		self.data = {
			file.stem: self._load_patient_xlsx(file)
			for file in self.path.glob("*.xlsx")
		}


	@staticmethod
	def _load_patient_xlsx(file: Path) -> dict[str, pd.DataFrame]:
		"""Load patients data from all sheets"""
		sheets = [Stage.BEFORE, Stage.DURING, Stage.AFTER]
		return {
			sheet: pd.read_excel(
				file, sheet_name = index, engine="openpyxl",
				header = None, skiprows = 1
			).to_numpy()
			for index, sheet in enumerate(sheets)
		}

	def all_pressures(self) -> dict[str, np.ndarray]:
		"""Return a dictionary of all patients' pressure data
			indexed by a unique key"""
		result = {}
		for code, stages in self.data.items():
			for stage, data in stages.items():
				result[f'{code}.{stage}'] = data[:, 1]

		return result

	def all_velocities(self) -> dict[str, np.ndarray]:
		"""Return a dictionary of all patients' velocity data
			indexed by a unique key"""
		result = {}
		for code, stages in self.data.items():
			for stage, data in stages.items():
				result[f'{code}.{stage}'] = data[:, 2]
		return result


class DatasetTest(unittest.TestCase):
	"""Testing `Dataset` class

	Attributes:
		dataset (utils.Dataset): AA patients' dataset used as a fixture
	"""
	def setUp(self):
		"""Load AA dataset"""
		self.dataset = Dataset('data/AA')


	def test_init(self):
		"""Test initialization of the object"""
		self.assertEqual(len(self.dataset.data), 5)
		self.assertIn('G2', self.dataset.data)
		self.assertEqual(self.dataset.data['G2'][Stage.BEFORE].shape, (1010, 3))

	def test_data(self):
		"""Test data retrieval"""
		pressures = self.dataset.all_pressures()
		self.assertEqual(len(pressures), 3 * 5)
		self.assertIn('G2.BEFORE', pressures)
		self.assertAlmostEqual(
			pressures['G2.BEFORE'][0], -14.1257, delta = 1e-4
		)
		self.assertAlmostEqual(
			pressures['G2.BEFORE'][-1], -11.6384, delta = 1e-4
		)

		velocities = self.dataset.all_velocities()
		self.assertEqual(len(velocities), 3 * 5)
		self.assertIn('G2.BEFORE', velocities)
		self.assertAlmostEqual(
			velocities['G2.BEFORE'][0], -0.0770, delta = 1e-4
		)
		self.assertAlmostEqual(
			velocities['G2.BEFORE'][-1], -0.0961, delta = 1e-4
		)

	# def tearDown(self):
		# ...

if __name__ == "__main__":
	unittest.main()
