# TODO : Transform this module into a builder (design pattern).
import pathlib

import fcg.voxsim
import fcg.voxsim.phantom as _phantom
import simulator.factory.geometry_factory.handlers as _sim_geom_handlers
import simulator.runner


def generate_fiber_tracts(
    voxsim_geom_params: _sim_geom_handlers.GeometryInfos, out_dir: pathlib.Path = fcg.voxsim.default.OUT_DIR
) -> None:
    # TODO : Supply SingularityConfig to SimulationRunner with custom attribute values
    simulation: simulator.runner.SimulationRunner = simulator.runner.SimulationRunner()

    simulation.generate_phantom(
        fcg.voxsim.default.SIMULATION_NAME, voxsim_geom_params, out_dir, output_nifti=_phantom.default.GENERATE_NIFTI
    )
