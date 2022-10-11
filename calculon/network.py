"""
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *  https://www.apache.org/licenses/LICENSE-2.0
 *
 * See the NOTICE file distributed with this work for additional information
 * regarding copyright ownership.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""


class Network:
  """Configuration for a network."""

  kNetOps = set(['p2p', 'reduce_scatter', 'all_gather', 'all_reduce'])

  @staticmethod
  def _valid_op(op, eff):
    valid = True
    if op not in Network.kNetOps:
      print(f'Invalid network op: {op}')
      valid = False
    if eff <= 0.0:
      print(f'Invalid network eff: {eff}')
      valid = False
    return valid

  def __init__(self, cfg):
    assert set(['bw', 'eff', 'size', 'ops']) == set(cfg.keys())
    self._bw = cfg['bw'] * 1e9  # Specified in GB/s
    assert self._bw > 0
    self._eff = cfg['eff']
    assert 0 < self._eff <= 1.0
    self._size = cfg['size']
    assert self._size >= 0
    self._ops = cfg['ops']
    assert all(Network._valid_op(k, v) for k, v in self._ops.items())
    assert set(self._ops.keys()) == Network.kNetOps

    # TODO(nicmcd): support reduction algorithms with (n-1)/n overhead scaling

  @property
  def size(self):
    return self._size

  def time(self, op, op_size, comm_size):
    """ Computes the time taken for a network operation.

    Args:
      op (str)        : operation name
      op_size (int)   : operation size in bytes
      comm_size (int) : number of participants in operation

    Returns:
      time (float)    : time needed for operation
    """
    if op == 'p2p':
      assert comm_size == 2
    else:
      assert comm_size > 1
    assert op in Network.kNetOps
    assert op_size >= 0
    return op_size / (self._bw * self._eff * self._ops[op])
